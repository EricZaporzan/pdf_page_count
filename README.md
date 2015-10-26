# pdf_page_count
Simple python script to sum the total number of pages of all the PDFs in a folder, or the page count of a single file, depending on the arguments passed when the function is called. 

## Usage
Running the script with no arguments, as ```python pdf_page_count```, will sum up all of the pages of all of the .pdf files in the current directory. 

Running the script with a pdf filename as the only argument, as ```python pdf_page_count /path/to/your/file.pdf``` will return the page count of that one file. 

Finally, running the script with a directory as the only argument, as ```python pdf_page_count /path/to/your/files/``` will sum up all of the pages of all of the .pdf files in that directory. 

## Acknowledgements

The code for counting pages of a single file came from http://stackoverflow.com/questions/16647746/how-to-count-the-numer-of-pdf-pages-in-python-that-has-blank-pdf-page-also 
