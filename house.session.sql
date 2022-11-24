-- SELECT name, neighbourhood_group, neighbourhood, room_type, price FROM tb_house
-- WHERE price < 100
-- ORDER BY price DESC
-- LIMIT 50;


-- SELECT price from  tb_house
-- WHERE price > 100
-- ORDER BY price DESC;


SELECT minimum_nights, number_of_reviews FROM tb_house

WHERE minimum_nights > 0 AND number_of_reviews > 0 
ORDER BY minimum_nights AND number_of_reviews
;