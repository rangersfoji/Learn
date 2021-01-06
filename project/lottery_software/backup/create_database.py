import mysql.connector

HOST = "lotteryboydb.c65i8rqfjo7h.us-east-1.rds.amazonaws.com"
PORT = 3306
USER = "lotteryboydb"
PASSWD = "K98Lp49p$K98Lp49p$"
DATABASE = "lotteryboydb"

db = mysql.connector.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,database=DATABASE)
c = db.cursor()


#create database
# c.execute(f"create database {database}")

# # lottery table
# c.execute("""create table if not exists lottery(
#     game_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     game_number int,
#     name varchar(50),
#     amount$ int,
#     total_ticket int
# )""")

# # active_book table
# c.execute("""create table if not exists active_book(
#     book_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     game_id int,
#     book_number int,
#     active_date date,
#     status varchar(10)
# )""")

# # daily_detail_report table
# c.execute("""create table if not exists daily_detail_report(
#     day_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     day_no int,
#     month_no int,
#     year_no int,
#     date date,
#     draw_sale float,
#     lottery_sold float,
#     lottery_cashing float,
#     commission float,
#     instant_sold float,
#     instant_suppose_to_be float,
#     difference float,
#     profit float
# )""")

# # detail_report table
# c.execute("""create table if not exists detail_report(
#     detail_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     day_no int,
#     book_number int,
#     ticket_number int,
#     sold_tickets int
# )""")

# # monthly_detail_report table
# c.execute("""create table if not exists monthly_detail_report(
#     month_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     month_no int,
#     year_no int,
#     profit float
# )""")

# # yearly_detail_report table
# c.execute("""create table if not exists yearly_detail_report(
#     year_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     year_no int,
#     profit float
# )""")

# # insert into lottery
# query = """insert into lottery(game_number,name,amount$,total_ticket) values(%s,%s,%s,%s)"""
# values = [
#     (218, 'diamond millions', 30, 50),
#     (180, 'fastest road to $1 million', 30, 50),
#     (150, '200x', 30, 50),
#     (118, 'ultimate millions', 30, 50),
#     (71, 'supreme millions', 30, 50),


#     (229, '10,000,000 bankroll', 20, 100),
#     (193, '5,000,000 100x cashword', 20, 100),
#     (131, '10,000,000 gold', 20, 100),
#     (58, '10,000,000 mega fortune', 20, 100),
#     ( 37, '10,000 a week for life!', 20, 100),
#     ( 25, '10,000,000 big money', 20, 100),


#     ( 261, '4,000,000 mega bucks', 10, 100),
#     ( 257, 'merry money blowout', 10, 100),
#     ( 225, '2,000,000 50x cashword', 10, 100),
#     ( 224, '$500 madness', 10, 100),
#     ( 221, '100x payout', 10, 100),
#     ( 212, '4,000,000 gold rush', 10, 100),
#     ( 207, 'cash in a flash', 10, 100),
#     ( 192, 'diamond 9', 10, 100),
#     ( 188, '100 x', 10, 100),
#     ( 160, '4,000,000 instant jackpot', 10, 100),
#     ( 145, '4,000,000 bonus cash', 10, 100),
#     ( 141, '200,000 a year for life!', 10, 100),
#     ( 122, 'hit 1000!', 10, 100),
#     ( 40, '4,000,000 payout', 10, 100),


#     ( 260, '7', 5, 150),
#     ( 223, '1,000,000 lucky', 5, 150),
#     ( 214, 'treasure hunt', 5, 150),
#     ( 213, '500,000 bonus link cashword', 5, 150),
#     ( 206, 'emerald 8', 5, 150),
#     ( 191, 'green gold', 5, 150),
#     ( 183, '100,000 a year for life!', 5, 150),
#     ( 178, '1,000,000 double jackpot', 5, 150),
#     ( 164, '1,000,000 platinum payout', 5, 150),
#     ( 159, 'make my month', 5, 150),
#     ( 146, 'corvette cash', 5, 150),
#     ( 144, '1,000,000 bonus cash', 5, 150),
#     ( 129, '$', 5, 150),
#     ( 117, '1,000,000 gold rush', 5, 150),
#     ( 105, 'road to riches', 5, 150),
#     ( 86, '1,000,000 payout', 5, 150),
#     ( 46, '1,000,000 jackpot', 5, 150),
#     ( 13, '1,000,000 players club', 5, 150),


#     ( 263, '100,000 silver', 2, 300),
#     ( 259, 'cash match', 2, 300),
#     ( 251, 'red ball tripler', 2, 300),
#     ( 227, 'bounus bar bingo', 2, 150),
#     ( 219, '20x payout', 2, 300),
#     ( 216, 'cash money', 2, 300),
#     ( 205, '100,000 cash explosion', 2, 300),
#     ( 182, '50,000 a year for life!', 2, 300),
#     ( 172, 'easy as 123', 2, 300),
#     ( 162, '24k madness', 2, 300),
#     ( 157, 'triple play', 2, 300),
#     ( 143, '100,000 bounus cash', 2, 300),
#     ( 139, 'power 7s', 2, 300),
#     ( 128, '100,000 triple diamonds', 2, 300),
#     ( 125, 'red hot $100,000', 2, 300),
#     ( 107, 'power play cashword', 2, 150),
#     ( 31, 'break the bank', 2, 300),
#     ( 16, '100,000 payout', 2, 300),


#     ( 262, 'electric 8s', 1, 300),
#     ( 258, 'luck of the irish tripler', 1, 300),
#     ( 253, '10,000 winter ice', 1, 300),
#     ( 226, 'lots of luck', 1, 300),
#     ( 142, '10,000 bounus cash', 1, 300),
#     ( 138, 'hot 5s', 1, 300),
#     ( 102, 'wild doubler', 1, 300),
#     ( 23, '500 a week for life', 1, 300)]
# c.executemany(query,values)

# db.commit()


def reset():
    c.execute("drop table if exists active_book , daily_detail_report, monthly_detail_report,yearly_detail_report,detail_report")
    db.commit()

    # active_book table
    c.execute("""create table if not exists active_book(
        book_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        game_id int,
        book_number int,
        active_date date,
        status varchar(10)
    )""")

    # daily_detail_report table
    c.execute("""create table if not exists daily_detail_report(
        day_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        day_no int,
        month_no int,
        year_no int,
        date date,
        draw_sale float,
        lottery_sold float,
        lottery_cashing float,
        commission float,
        instant_sold float,
        instant_suppose_to_be float,
        difference float,
        profit float
    )""")

    # detail_report table
    c.execute("""create table if not exists detail_report(
        detail_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        day_no int,
        book_number int,
        ticket_number int,
        sold_tickets int
    )""")

    # monthly_detail_report table
    c.execute("""create table if not exists monthly_detail_report(
        month_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        month_no int,
        year_no int,
        profit float
    )""")

    # yearly_detail_report table
    c.execute("""create table if not exists yearly_detail_report(
        year_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        year_no int,
        profit float
    )""")

    db.commit()

    print("database reseted.")


reset()