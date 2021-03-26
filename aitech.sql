CREATE TABLE data_spot (
spot_id SERIAL PRIMARY KEY,
spot_area TEXT,
spot_name TEXT,
spot_latitude TEXT,
spot_longitude TEXT,
spot_history_culture INTEGER,
spot_food_product INTEGER,
spot_nature INTEGER,
spot_view INTEGER,
spot_illumination INTEGER,
spot_experience INTEGER,
spot_opentime INTEGER,
spot_closetime INTEGER,
spot_stayingtime INTEGER
);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude,spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime) 
VALUES ('東京', '皇居', '35.6802117', '139.7576692',1, 0, 1, 1, 1, 0, 0, 24, 1);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude,spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime) 
VALUES ('東京', '東京駅', '35.6809591', '139.7673068', 1, 1, 0, 1, 1, 0, 5, 24, 1);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime) 
VALUES ('東京', 'スカイツリー', '35.7100069', '139.8108103', 0, 1, 0, 1, 1, 1, 9, 21, 3);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('東京', '東京タワー', '35.658584', '139.7454316', 1, 1, 0, 1, 0, 1, 10.5, 21.5, 3);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('東京', 'ハチ公前', '35.6590439', '139.7005917', 1, 0, 0, 1, 1, 0, 0, 0, 0.5);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('東京', '六本木ヒルズ', '35.6603976', '139.7292361', 0, 1, 0, 0, 1, 0, 0, 1);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('東京', '高尾山', '35.6254527', '139.2437982', 1, 1, 1, 1, 0, 0, 8, 17, 10);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('神奈川', '赤レンガ倉庫', '35.4516872', '139.6437905', 1, 1, 0, 1, 1, 0, 10, 20, 1);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('東京', 'お台場海浜公園', '35.6313051', '139.7777839', 0, 1, 1, 1, 1, 0, 0, 0, 2);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('神奈川', '江ノ島', '35.3110403', '139.4875402', 0, 1, 1, 1, 1, 0, 5, 22, 3);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('神奈川', '高徳院(鎌倉大仏)', '35.3168463', '139.5357335', 0, 1, 0, 0, 0, 0, 8, 17, 1);
INSERT INTO data_spot (
spot_area, spot_name, spot_latitude, spot_longitude, spot_history_culture, spot_food_product, 
spot_nature, spot_view, spot_illumination, spot_experience, spot_opentime, spot_closetime)
VALUES ('東京', '浅草寺', '35.7146576', '139.7967813', 1, 1, 0, 1, 1, 0, 0, 0, 1);