# Author : Mohammad Sheikh Ghazanfar (https://github.com/msghera)

# I hereby declare that, the author accepts no responsibility for
# the topicality, correctness, completeness or quality of the
# the code. Also, using this code is propieratorily protected for
# https://github.com/msghera/bangla-programming-resources.


import os
import logging
import requests
import markdown
from lxml import etree
import json
from alive_progress import alive_bar
import pandas
import time

logging.basicConfig(
    format="[%(asctime)s] : %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class LinkTester:
    def __init__(self, filepath, **kwargs):

        self.filepath = filepath
        self.only_error = kwargs.get("only_error", False)
        self.output_filename = kwargs.get("output_filename", None)

        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "referer": "https://www.google.com/",
        }

        logger.info(f"Initiating LinkTester for : {self.filepath}\n")

        if self.filepath is None:
            raise "Filepath can not be None"
        try:
            with open(self.filepath, "r", encoding="utf8") as file:
                self.lines = file.read().split("\n")
        except IOError:
            raise f"Error occured while opening or reading the file {self.filepath}."

        with alive_bar(len(self.lines)) as bar:
            for line_id in range(len(self.lines)):
                self.lines[line_id] = self.__link_extractor(self.lines[line_id])

                for i in range(len(self.lines[line_id])):
                    try:
                        self.lines[line_id][i]["result"] = self.__link_tester(
                            self.lines[line_id][i]["link"], line_id+1
                        )
                    except:
                        logger.info(f"LinkTester failed to test at line : {line_id+1}\n")

                bar()

        self.__generate_report()

    def __link_extractor(self, line):

        if len(line) == 0:
            return []
        else:
            line = line.strip()

        doc, ret = etree.fromstring(markdown.markdown(line)), []
        for link in doc.xpath("//a"):
            cur = {"text": link.text, "link": link.get("href")}

            ret.append(cur)

        return ret

    def __link_tester(self, link, line_number):

        response = None
        try:
            response = requests.get(link, headers=self.header)
            response = {
                "responded": True,
                "status_code": f"Status Code : {response.status_code}",
                "is_okay": (response.status_code // 100) == 2,
            }

        except Exception as exception:
            response = {"responded": False, "status_code": f"Issue : {exception}"}

        broken_statement = f"Broken link found at line : {line_number}.\n"
        if response["responded"]:
            if not response["is_okay"]:
                logger.info(broken_statement)

        else:
            logger.info(broken_statement)

        time.sleep(2)
        return response

    def __generate_report(self):
        line_number, response_type, text, link = [], [], [], []

        for line_id in range(len(self.lines)):

            line = self.lines[line_id]
            for each in line:

                if (
                    self.only_error
                    and each["result"]["responded"]
                    and each["result"].get("is_okay", False)
                ):
                    continue

                line_number.append(line_id)

                if each["result"]["responded"]:
                    if each["result"]["is_okay"]:
                        response_type.append("Okay")
                    else:
                        response_type.append("Error Response")
                else:
                    response_type.append("No Response")

                text.append(each["text"])
                link.append(each["link"])

        if self.output_filename is None:
            self.output_filename = (
                os.path.basename(self.filepath.split()[0]) + "_LinkTesterResult.csv"
            )

        try:
            pandas.DataFrame(
                {
                    "Line Number": line_number,
                    "Response Type": response_type,
                    "Text for Link": text,
                    "Link": link,
                }
            ).to_csv(self.output_filename, index=False)

        except:
            raise "Issue in Output file creation."

        total_broken_links = len(response_type) - sum(
            [1 for res in response_type if res == "Okay"]
        )
        logger.info(
            f"\nLink Test is completed. Total {total_broken_links} link(s) found as broken out of {len(response_type)}. Detailed Report can be found at : {self.output_filename}\n"
        )


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = [f for f in os.listdir("../") if f.split(".")[-1] == "md"]
    filepaths = [os.path.abspath(os.path.join(dir_path, os.pardir, f)) for f in files]

    for file in filepaths:
        LinkTester(file)


if __name__ == "__main__":
    main()
