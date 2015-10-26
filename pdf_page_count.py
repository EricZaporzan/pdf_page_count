import re, os, glob, sys

rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)

def count_pages(filename):
    data = file(filename,"rb").read()
    return len(rxcountpages.findall(data))

def sum_pages(args):
    if len(args) > 1:
        if args[1].endswith(".pdf"):
            return count_pages(args[1])
        else:
            os.chdir(args[1])
    total_pages = 0
    fnames = glob.glob("./*.pdf")
    for fname in fnames:
        total_pages = total_pages + count_pages(fname)
    return total_pages

if __name__=="__main__":
    print(sum_pages(sys.argv))
