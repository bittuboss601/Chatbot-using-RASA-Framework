## greet + show_phones
* greet
  - utter_how_can_I_help
* buy_phone_laptop{"category":"phone"}
  - product_search_form
  - form{"name":"product_search_form"}
  - form{"name":null}
* goodbye
  - utter_goodbye

## greet + show_latest_news
* greet
  - utter_how_can_I_help
* latest_news_phones_laptops{"category":"phone"}
  - action_show_latest_news
* goodbye
  - utter_goodbye
