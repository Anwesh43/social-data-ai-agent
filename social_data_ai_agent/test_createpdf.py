from tools.social_data_tools import createPDFFromHTMLStr

def testHTMLToPdf():
    with open("test.html", "r") as f:
        html = f.read()
        createPDFFromHTMLStr(html, "testhtml.pdf")
        print("printing pdf in testhtml.pdf")


if __name__ == "__main__":
    testHTMLToPdf()