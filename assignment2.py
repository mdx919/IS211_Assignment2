import csv, urllib.request, datetime, logging, argparse, sys

personData = {}

assignment2 = 'errors.log'
logging.basicConfig(
    filename=assignment2,
    level=logging.ERROR,
)

def downloadData(url):
    # uncomment below code to make url based csv file to work
    try:
        response = urllib.request.urlopen(url)
        lines = [l.decode('utf-8') for l in response.readlines()]
        csvData = csv.reader(lines)
        personData = processData(csvData)
        return personData
    except ValueError:
        print('Error processing the CSV file')
        sys.exit()

    # uncomment below code to make local file to work
    # try:
    #     with open('data.csv', newline='') as csvfile:
    #         csvData = csv.reader(csvfile, delimiter=',', quotechar='|')
    #         personData = processData(csvData)
    #         return personData
    # except ValueError:
    #     print('Error processing the CSV file')
    #     sys.exit()

def processData(data):
    result = {}

    for i, row in enumerate(data):
        validateDate = checkDate(row[2], i, row[0])
        if i is not 0 and validateDate is not False:
            result[row[0]] = (row[1], validateDate)
    return result


def checkDate(date, linenum, id):
    try:
        formattedDate = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        return formattedDate
    except ValueError:
        logging.error(' Error processing line {linenum} for ID {id}'.format(linenum = linenum, id = id))
        return False

def displayPerson(pid, data):
    for key in data:
        if pid in data:
            return data[pid]

parser = argparse.ArgumentParser()
parser.add_argument("--url")
args = parser.parse_args()
if len(sys.argv) < 2 or sys.argv[1] != '--url':
    sys.exit()
elif len(sys.argv) > 1 and sys.argv[1] == '--url':
    data = downloadData(args)

    while True:
        print('Enter an ID to look up:')
        pid = input()
        if int(pid) <= 0:
            print('Invalid ID number')
            sys.exit()
        elif int(pid) > 0:
            print(displayPerson(pid, data))

# 'http://winterolympicsmedals.com/medals.csv'