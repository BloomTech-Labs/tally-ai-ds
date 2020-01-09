# tallylib/sql.py
# Local
from yelp.models import YelpReview

def getYelpReviews(business_id, 
                   starting_date, 
                   ending_date):
    sql = f'''
    SELECT uuid, date, text FROM tallyds.review
    WHERE business_id = '{business_id}'
    AND datetime >= '{starting_date}'
    AND datetime <= '{ending_date}';
    '''
    return [[record.date, record.text] for record in YelpReview.objects.raw(sql)]