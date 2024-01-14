game_code = 'G_SPD' # game code is

list_wotan_delabs = [
   'dau_day','nru_ru_day','job_status'
]

setting = {
   'nru_ru' :{
      'web' : {
         'is_country_valid' : False,
         'is_os_valid' : True,
         'dog' : 'love'
      }, 
      'app' : {
         'is_country_valid' : True,
         'is_os_valid' : True
      }
   },
   'dau_day' :{
      'web' : {
         'is_country_valid' : False,
         'is_os_valid' : True
      }, 
      'app' : {
         'is_country_valid' : True,
         'is_os_valid' : True,
         'cat' : 'loved'
      }
   }
}

# %%

s3_setting = {"game_code":{"0":"G_SPD","1":"G_SPD","2":"G_SPD","3":"G_SPD","4":"G_SPD","5":"G_SPD","6":"G_SPD","7":"G_SPD","8":"G_SPD","9":"G_SPD","10":"G_SPD","11":"G_SPD","12":"G_SPD","13":"G_SPD","14":"G_SPD","15":"G_SPD","16":"G_SPD","17":"G_SPD","18":"G_SPD","19":"G_SPD","20":"G_SPD","21":"G_SPD","22":"G_SPD","23":"G_SPD","24":"G_SPD","25":"G_SPD","26":"G_SPD","27":"G_SPD","28":"G_SPD","29":"G_SPD","30":"G_SPD","31":"G_SPD","32":"G_SPD","33":"G_SPD","34":"G_SPD","35":"G_SPD","36":"G_SPD","37":"G_SPD","38":"G_SPD","39":"G_SPD","40":"G_SPD","41":"G_SPD","42":"G_SPD","43":"G_SPD","44":"G_SPD","45":"G_SPD","46":"G_SPD","47":"G_SPD","48":"G_SPD","49":"G_SPD","50":"G_SPD","51":"G_SPD","52":"G_SPD","53":"G_SPD","54":"G_SPD"},"game_name":{"0":"rumble-racing","1":"rumble-racing","2":"rumble-racing","3":"rumble-racing","4":"rumble-racing","5":"rumble-racing","6":"rumble-racing","7":"rumble-racing","8":"rumble-racing","9":"rumble-racing","10":"rumble-racing","11":"rumble-racing","12":"rumble-racing","13":"rumble-racing","14":"rumble-racing","15":"rumble-racing","16":"rumble-racing","17":"rumble-racing","18":"rumble-racing","19":"rumble-racing","20":"rumble-racing","21":"rumble-racing","22":"rumble-racing","23":"rumble-racing","24":"rumble-racing","25":"rumble-racing","26":"rumble-racing","27":"rumble-racing","28":"rumble-racing","29":"rumble-racing","30":"rumble-racing","31":"rumble-racing","32":"rumble-racing","33":"rumble-racing","34":"rumble-racing","35":"rumble-racing","36":"rumble-racing","37":"rumble-racing","38":"rumble-racing","39":"rumble-racing","40":"rumble-racing","41":"rumble-racing","42":"rumble-racing","43":"rumble-racing","44":"rumble-racing","45":"rumble-racing","46":"rumble-racing","47":"rumble-racing","48":"rumble-racing","49":"rumble-racing","50":"rumble-racing","51":"rumble-racing","52":"rumble-racing","53":"rumble-racing","54":"rumble-racing"},"db_name":{"0":"ldb","1":"ldb","2":"ldb","3":"ldb","4":"ldb","5":"ldb","6":"ldb","7":"ldb","8":"ldb","9":"ldb","10":"ldb","11":"ldb","12":"ldb","13":"ldb","14":"ldb","15":"ldb","16":"ldb","17":"ldb","18":"ldb","19":"ldb","20":"ldb","21":"ldb","22":"ldb","23":"ldb","24":"ldb","25":"ldb","26":"ldb","27":"ldb","28":"ldb","29":"ldb","30":"ldb","31":"ldb","32":"ldb","33":"ldb","34":"ldb","35":"ldb","36":"ldb","37":"ldb","38":"ldb","39":"ldb","40":"ldb","41":"ldb","42":"ldb","43":"ldb","44":"ldb","45":"ldb","46":"ldb","47":"ldb","48":"ldb","49":"ldb","50":"ldb","51":"ldb","52":"ldb","53":"global","54":"platform"},"is_total":{"0":True,"1":False,"2":True,"3":True,"4":True,"5":True,"6":True,"7":True,"8":True,"9":True,"10":True,"11":True,"12":True,"13":True,"14":True,"15":True,"16":True,"17":True,"18":True,"19":True,"20":True,"21":True,"22":False,"23":True,"24":True,"25":True,"26":True,"27":True,"28":True,"29":True,"30":True,"31":True,"32":False,"33":True,"34":True,"35":True,"36":True,"37":False,"38":True,"39":True,"40":True,"41":True,"42":True,"43":True,"44":False,"45":False,"46":True,"47":True,"48":True,"49":False,"50":True,"51":True,"52":True,"53":False,"54":False},"table_name":{"0":"log_login_detail","1":"log_cash_purchase","2":"log_league_change","3":"log_star","4":"log_battle_ready","5":"log_battle_room_begin","6":"log_battle_room_end","7":"log_battle_user_begin","8":"log_battle_user_end","9":"log_tournament_join","10":"log_levelup","11":"log_victory_point","12":"log_victory_point_reward","13":"log_asset_change","14":"log_tournament_join","15":"log_levelup","16":"log_victory_point","17":"log_victory_point_reward","18":"log_asset_unlock","19":"log_collection","20":"log_achievement","21":"log_sticker_attach","22":"log_sticker","23":"log_alnumn_complete_total","24":"log_sticker_trade_request","25":"log_sticker_trade_accept","26":"log_sticker_trade_cancel","27":"log_career_stat","28":"log_soft_crypto","29":"log_fuel_charge","30":"log_kart_add","31":"log_driver","32":"log_costume_add/","33":"log_license_plate","34":"log_looks_apply","35":"log_looks_delete","36":"log_looks_reset","37":"log_club_manage","38":"log_race_pass_upgrade","39":"log_race_pass_reward","40":"log_race_pass_take_req","41":"log_race_pass_ticket","42":"log_buy_product","43":"log_shop_reset","44":"log_login_detail","45":"log_ccu","46":"log_tutorial","47":"log_mail_take","48":"log_event_reward_take","49":"log_rank_event_reward","50":"log_rttstat","51":"log_abuse_general","52":"log_abuse_speed","53":"xsolla_payout_transaction_completion","54":"plt_rrs_user_login"},"s3_path":{"0":"s3://wotan-data/rumble-racing/log_login_detail/","1":"s3://wotan-data/rumble-racing/log_cash_purchase/","2":"s3://wotan-data/rumble-racing/log_league_change/","3":"s3://wotan-data/rumble-racing/log_star/","4":"s3://wotan-data/rumble-racing/log_battle_ready/","5":"s3://wotan-data/rumble-racing/log_battle_room_begin/","6":"s3://wotan-data/rumble-racing/log_battle_room_end/","7":"s3://wotan-data/rumble-racing/log_battle_user_begin/","8":"s3://wotan-data/rumble-racing/log_battle_user_end/","9":"s3://wotan-data/rumble-racing/log_tournament_join/","10":"s3://wotan-data/rumble-racing/log_levelup/","11":"s3://wotan-data/rumble-racing/log_victory_point/","12":"s3://wotan-data/rumble-racing/log_victory_point_reward/","13":"s3://wotan-data/rumble-racing/log_asset_change/","14":"s3://wotan-data/rumble-racing/log_tournament_join/","15":"s3://wotan-data/rumble-racing/log_levelup/","16":"s3://wotan-data/rumble-racing/log_victory_point/","17":"s3://wotan-data/rumble-racing/log_victory_point_reward/","18":"s3://wotan-data/rumble-racing/log_asset_unlock/","19":"s3://wotan-data/rumble-racing/log_collection/","20":"s3://wotan-data/rumble-racing/log_achievement/","21":"s3://wotan-data/rumble-racing/log_sticker_attach/","22":"s3://wotan-data/rumble-racing/log_sticker/","23":"s3://wotan-data/rumble-racing/log_alnumn_complete_total/","24":"s3://wotan-data/rumble-racing/log_sticker_trade_request/","25":"s3://wotan-data/rumble-racing/log_sticker_trade_accept/","26":"s3://wotan-data/rumble-racing/log_sticker_trade_cancel/","27":"s3://wotan-data/rumble-racing/log_career_stat/","28":"s3://wotan-data/rumble-racing/log_soft_crypto/","29":"s3://wotan-data/rumble-racing/log_fuel_charge/","30":"s3://wotan-data/rumble-racing/log_kart_add/","31":"s3://wotan-data/rumble-racing/log_driver/","32":"s3://wotan-data/rumble-racing/log_costume_add//","33":"s3://wotan-data/rumble-racing/log_license_plate/","34":"s3://wotan-data/rumble-racing/log_looks_apply/","35":"s3://wotan-data/rumble-racing/log_looks_delete/","36":"s3://wotan-data/rumble-racing/log_looks_reset/","37":"s3://wotan-data/rumble-racing/log_club_manage/","38":"s3://wotan-data/rumble-racing/log_race_pass_upgrade/","39":"s3://wotan-data/rumble-racing/log_race_pass_reward/","40":"s3://wotan-data/rumble-racing/log_race_pass_take_req/","41":"s3://wotan-data/rumble-racing/log_race_pass_ticket/","42":"s3://wotan-data/rumble-racing/log_buy_product/","43":"s3://wotan-data/rumble-racing/log_shop_reset/","44":"s3://wotan-data/rumble-racing/log_login_detail/","45":"s3://wotan-data/rumble-racing/log_ccu/","46":"s3://wotan-data/rumble-racing/log_tutorial/","47":"s3://wotan-data/rumble-racing/log_mail_take/","48":"s3://wotan-data/rumble-racing/log_event_reward_take/","49":"s3://wotan-data/rumble-racing/log_rank_event_reward/","50":"s3://wotan-data/rumble-racing/log_rttstat/","51":"s3://wotan-data/rumble-racing/log_abuse_general/","52":"s3://wotan-data/rumble-racing/log_abuse_speed/","53":"s3://wotan-data/rumble-racing/xsolla_payout_transaction_completion/","54":"s3://wotan-data/rumble-racing/plt_rrs_user_login/"},"s_folder":{"0":"rumble-racing/log_login_detail/","1":"rumble-racing/log_cash_purchase/","2":"rumble-racing/log_league_change/","3":"rumble-racing/log_star/","4":"rumble-racing/log_battle_ready/","5":"rumble-racing/log_battle_room_begin/","6":"rumble-racing/log_battle_room_end/","7":"rumble-racing/log_battle_user_begin/","8":"rumble-racing/log_battle_user_end/","9":"rumble-racing/log_tournament_join/","10":"rumble-racing/log_levelup/","11":"rumble-racing/log_victory_point/","12":"rumble-racing/log_victory_point_reward/","13":"rumble-racing/log_asset_change/","14":"rumble-racing/log_tournament_join/","15":"rumble-racing/log_levelup/","16":"rumble-racing/log_victory_point/","17":"rumble-racing/log_victory_point_reward/","18":"rumble-racing/log_asset_unlock/","19":"rumble-racing/log_collection/","20":"rumble-racing/log_achievement/","21":"rumble-racing/log_sticker_attach/","22":"rumble-racing/log_sticker/","23":"rumble-racing/log_alnumn_complete_total/","24":"rumble-racing/log_sticker_trade_request/","25":"rumble-racing/log_sticker_trade_accept/","26":"rumble-racing/log_sticker_trade_cancel/","27":"rumble-racing/log_career_stat/","28":"rumble-racing/log_soft_crypto/","29":"rumble-racing/log_fuel_charge/","30":"rumble-racing/log_kart_add/","31":"rumble-racing/log_driver/","32":"rumble-racing/log_costume_add//","33":"rumble-racing/log_license_plate/","34":"rumble-racing/log_looks_apply/","35":"rumble-racing/log_looks_delete/","36":"rumble-racing/log_looks_reset/","37":"rumble-racing/log_club_manage/","38":"rumble-racing/log_race_pass_upgrade/","39":"rumble-racing/log_race_pass_reward/","40":"rumble-racing/log_race_pass_take_req/","41":"rumble-racing/log_race_pass_ticket/","42":"rumble-racing/log_buy_product/","43":"rumble-racing/log_shop_reset/","44":"rumble-racing/log_login_detail/","45":"rumble-racing/log_ccu/","46":"rumble-racing/log_tutorial/","47":"rumble-racing/log_mail_take/","48":"rumble-racing/log_event_reward_take/","49":"rumble-racing/log_rank_event_reward/","50":"rumble-racing/log_rttstat/","51":"rumble-racing/log_abuse_general/","52":"rumble-racing/log_abuse_speed/","53":"rumble-racing/xsolla_payout_transaction_completion/","54":"rumble-racing/plt_rrs_user_login/"}}
# %%
s3_setting
# %%

# %%
