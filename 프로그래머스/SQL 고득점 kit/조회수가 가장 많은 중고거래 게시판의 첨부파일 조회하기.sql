# concat을 사용해서 붙인다

SELECT concat('/home/grep/src/', B.BOARD_ID, '/', B.FILE_ID, B.FILE_NAME, B.FILE_EXT) AS FILE_PATH
from USED_GOODS_BOARD A join USED_GOODS_FILE B on A.BOARD_ID = B.BOARD_ID
where B.BOARD_ID = (select BOARD_ID from USED_GOODS_BOARD order by VIEWS DESC LIMIT 1)
order by B.FILE_ID desc