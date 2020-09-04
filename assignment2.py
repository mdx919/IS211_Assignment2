import csv, urllib.request, datetime, logging

assignment2 = 'dateErrorLogs.out'
logging.basicConfig(
    filename=assignment2,
    level=logging.ERROR,
)

def downloadData(url):
    # response = urllib.request.urlopen(url)
    # lines = [l.decode('utf-8') for l in response.readlines()]
    # csvData = csv.reader(lines)
    #
    # data = processData(csvData)
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        data = processData(spamreader)
        print(data)

def processData(data):
    result = {}
    for i, row in enumerate(data):
        validateDate = checkDate(row[2], i, row[0])
        print(validateDate)
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

downloadData('http://winterolympicsmedals.com/medals.csv')