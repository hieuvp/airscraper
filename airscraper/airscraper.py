import argparse
import functions


def get_base_csv(api_key, base_id, table_name, view_name):
    if base_id is None:
        info = {"daily coffee api error": {"error": "please pass a base_id value"}}
        code = 400
        return info, code
    elif base_id == '<your_base_id>':
        info = {
            "info": "<your_base_id> is an example value. Please visit https://grdc.notion.site/CSV-Exporter-for-Airtable-16afca474b954f588eff2e6b91620a4a to see how you can enable this api to work with your own Airtable base id"}
        code = 400
        return info, code

    if api_key is None:
        info = {"daily coffee api error": {"error": "please pass an api_key value"}}
        code = 400
        return info, code
    elif api_key == '<your_api_key>':
        info = {
            "info": "<your_api_key> is an example value. Please visit https://grdc.notion.site/CSV-Exporter-for-Airtable-16afca474b954f588eff2e6b91620a4a to see how you can enable this api to work with your own Airtable api key"}
        code = 400
        return info, code

    if table_name is None:
        info = {"daily coffee api error": {"error": "please pass a table_name value"}}
        code = 400
        return info, code

    table_name.replace(' ', '%20')

    error_log = None

    try:
        info, code, df = functions.get_df(api_key=api_key, base_id=base_id, table_name=table_name, view_name=view_name)
    except Exception as e:
        error_log = str(e)
        # print this error log for debug
        info = {"daily coffee api error": {"error": "Something went wrong."}}
        code = 400
        df = None

    if code != 200:
        return info, code
    else:
        resp = df.to_csv(index=False)
        return resp


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Download CSV from Airtable. You can pass the result to file using '> name.csv'",
        prog="airscraper")

    parser.add_argument('--key', default=None)
    parser.add_argument('--base', default=None)
    parser.add_argument('--table', default=None)
    parser.add_argument('--view', default=None)

    args = parser.parse_args()

    print(
        get_base_csv(api_key=args.key, base_id=args.base, table_name=args.table, view_name=args.view))
