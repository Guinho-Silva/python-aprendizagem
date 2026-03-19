SELECT seller_id,
    SUM(t1.price) AS TotalRevenue,
    COUNT(DISTINCT t1.order_id) as qtSalles
FROM tb_orders AS t1
GROUP BY seller_id


-- trocar o seller, pois não existe essa coluna

