#! python3
# -*- coding:utf-8 -*-
from google.cloud.vision import types
from google.cloud import vision
import sys
import io
import os
import re
import cv2
import MeCab

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', authJsonFile)

# Imports the Google Cloud client library


def detect_label(path, debug=True):
    # check args that image path exists
    if path == None:
        print("please input target image file on first argument.")
        sys.exit(0)

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath(path)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    if debug == True:
        print('Labels:')
        for label in labels:
            print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return labels


def detect_text(path, debug=True):
    # check args that image path exists
    if path == None:
        print("please input target image file on first argument.")
        sys.exit(0)

    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if debug == True:
        print('Texts:')
        for text in texts:
            print('\n"{}"'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                         for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return texts


def detect_document(path, debug=True):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    if debug == True:
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                print('\nBlock confidence: {}\n'.format(block.confidence))

                for paragraph in block.paragraphs:
                    print('Paragraph confidence: {}'.format(
                        paragraph.confidence))

                    for word in paragraph.words:
                        word_text = ''.join([
                            symbol.text for symbol in word.symbols
                        ])
                        print('Word text: {} (confidence: {})'.format(
                            word_text, word.confidence))

                        for symbol in word.symbols:
                            print('\tSymbol: {} (confidence: {})'.format(
                                symbol.text, symbol.confidence))


def localize_objects(path, debug=True):
    """Localize objects in the local image.
    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    if debug == True:
        print('Number of objects found: {}'.format(len(objects)))
        for object_ in objects:
            print('\n{} (confidence: {})'.format(object_.name, object_.score))
            print('Normalized bounding polygon vertices: ')
            for vertex in object_.bounding_poly.normalized_vertices:
                print(' - ({}, {})'.format(vertex.x, vertex.y))

    return objects


func_list = {}
func_list.setdefault('label', detect_label)
func_list.setdefault('text', detect_text)
func_list.setdefault('document', detect_document)
func_list.setdefault('objects', localize_objects)

if __name__ == '__main__':
    runFunc = func_list.get(sys.argv[2], None)
    if runFunc != None:
        # draw bounds
        img = cv2.imread(sys.argv[1])

        if sys.argv[2] == 'label':
            labels = runFunc(sys.argv[1])
            for label in labels:
                print("description:" + label.description + "  score:" + str(label.score))

        if sys.argv[2] == 'text':
            texts = runFunc(sys.argv[1], bool(int(sys.argv[4])))

            tagger = MeCab.Tagger()
            tagger.parse('')
            searches = None
            if len(sys.argv) > 4:
                searches = [re.compile(sys.argv[3])]
                node = tagger.parseToNode(sys.argv[3])
                while node:
                    if "BOS" not in node.feature and "EOS" not in node.feature and \
                       node.feature.split(",")[0] not in ["助詞", "助動詞"]:
                        searches.append(re.compile(node.surface))
                    node = node.next

            for i, text in enumerate(texts):
                # restricting draw text include search words.
                if searches is not None:
                    hasWords = False
                    for b in searches:
                        if b.search(text.description) is not None:
                            hasWords = True
                            break
                    if hasWords == False:
                        if i == 0:
                            break
                        else:
                            continue

                # draw rect
                vertices = []
                [vertices.append((verticex.x, verticex.y)) for verticex in text.bounding_poly.vertices]
                cv2.rectangle(img, (vertices[0][0], vertices[0][1]), (vertices[2][0], vertices[2][1]), (0, 255, 0), 6)

            fname = os.path.dirname(os.path.abspath(sys.argv[1])) + os.path.sep + "after_bounds.jpg"
            cv2.imwrite(fname, img)

        if sys.argv[2] == 'objects':
            objects = runFunc(sys.argv[1], bool(int(sys.argv[3])))

            for object_ in objects:
                # draw rect
                vertices = []
                [vertices.append((vertex.x, vertex.y)) for vertex in object_.bounding_poly.normalized_vertices]
                x = int(vertices[0][0] * img.shape[1])
                y = int(vertices[0][1] * img.shape[0])
                width = int(vertices[2][0] * img.shape[1])
                height = int(vertices[2][1] * img.shape[1])

                cv2.rectangle(img, (x, y), (width, height), (0, 255, 0), 6)

            fname = os.path.dirname(os.path.abspath(sys.argv[1])) + os.path.sep + "after_bounds.jpg"
            cv2.imwrite(fname, img)
