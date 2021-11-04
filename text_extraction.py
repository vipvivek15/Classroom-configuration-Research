import io
from pdfminer.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator,TextConverter

def pdftotext(path):
   resource_manager = PDFResourceManager()
   file_handle = io.StringIO()
   laprams = LAParams(word_margin=1.0,boxes_flow=0.5,char_margin=2.0,line_overlap=0.5,line_margin=0.5)
   converter = TextConverter(resource_manager,file_handle, laparams=laprams)
   page_interpreter = PDFPageInterpreter(resource_manager,converter)
   i = 1
   with open(path,'rb') as fh:
      for page in PDFPage.get_pages(fh,caching=False,check_extractable=True):
        page_interpreter.process_page(page)
        
      text = file_handle.getvalue()

   converter.close()
   file_handle.close()

   return text

raw = pdftotext('sample.pdf')
with open('sample.txt','w') as f:
    f.write(raw)