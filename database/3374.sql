CREATE FUNCTION CapitalizeWords(str TEXT) RETURNS TEXT DETERMINISTIC
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE word TEXT;
    DECLARE result TEXT DEFAULT '';

    WHILE LENGTH(str) > 0 DO
        SET word = TRIM(SUBSTRING_INDEX(str, ' ', 1));
        IF LENGTH(word) > 0 THEN
            SET result = CONCAT(result, ' ', UPPER(LEFT(word, 1)), LOWER(SUBSTRING(word, 2)));
        END IF;
        SET str = SUBSTRING(str FROM LENGTH(word) + 2);
    END WHILE;

    RETURN TRIM(result);
END;


UPDATE users
SET name = CapitalizeWords(name);
