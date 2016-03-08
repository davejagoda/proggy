#!/usr/bin/python

# based on this:
# http://www.cs.cmu.edu/~benhdj/Mac/splitPDF.py
# by benhdj@cs.cmu.edu (Benjamin Han)

import argparse
import os
import CoreGraphics

def validate_size(dimensions, verbose=False):
    for dimension in dimensions:
        if verbose: print('validating dimension:{}'.format(dimension))
        assert dimension in (612, 792, 1008, 1224)

def process_pdf(file, verbose=False):
    if os.path.isfile(file):
        input_doc = CoreGraphics.CGPDFDocumentCreateWithProvider(CoreGraphics.CGDataProviderCreateWithFilename(file))
        if input_doc:
            max_pages = input_doc.getNumberOfPages()
            page_number_width = len(str(max_pages))
            print('file:{} has {} pages'.format(file, max_pages))
            for page_num in range(1, max_pages + 1):
                media_box = input_doc.getPage(page_num).getBoxRect(CoreGraphics.kCGPDFMediaBox)
                width  = int(round(media_box.getWidth(), 1))
                height = int(round(media_box.getHeight(), 1))
                validate_size([width, height], verbose)
                page_rect = CoreGraphics.CGRectMake (0, 0, width, height)
                (prefix, suffix) = os.path.splitext(os.path.basename(file))
                new_file = '{}.page{}{}'.format(prefix, str(page_num).zfill(page_number_width), suffix)
                if verbose: print('{} width:{} height:{}'.format(new_file, width, height))
                write_context = CoreGraphics.CGPDFContextCreateWithFilename(new_file, page_rect)
                write_context.beginPage(media_box)
                write_context.drawPDFDocument(media_box, input_doc, page_num)
                write_context.endPage()
        else:
            print('could not determine number of pages')
    else:
        print('could not open file:{}'.format(file))

if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='pdf file to split into single pages')
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()
    process_pdf(args.file, args.verbose)
