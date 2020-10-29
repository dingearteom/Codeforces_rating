from get_contests_id import get_contests_id
from set_nicknames import write_nicknames
from CF_API import data_all_contests, sort_data
from excel import write_excel
from Google_Dirve_API import load_google_drive

if __name__ == '__main__':
    get_contests_id()
    write_nicknames()

    data = sort_data(data_all_contests())
    write_excel(data)

    load_google_drive()


