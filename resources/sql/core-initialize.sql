TRUNCATE TABLE expense_payment_origin_transaction;
TRUNCATE TABLE expense_payment;
TRUNCATE TABLE one_time_expense;
TRUNCATE TABLE recurring_expense;
TRUNCATE TABLE expense_recipient;

INSERT INTO expense_recipient (id,"name") VALUES
	 ('a03b3b1c-06cd-4b1f-99fc-cb619da44378','Destinatario desconocido'),
	 ('3fa85f64-5717-4562-b3fc-2c963f66afa6','Ana Pérez Martínez'),
	 ('94ba6d13-6b63-40cc-ae05-8025457277cd','Renfe'),
	 ('103b184f-0da5-4f5e-94b7-c7970c8cd2e4','Movistar'),
	 ('0752ca23-b729-471a-bab5-c7659cad12f1','Spotify');

INSERT INTO one_time_expense (id,user_id,status,category,recipient_id,concept,"comments",amount,amount_type,payment_method,hidden_in_plans,payment_id,created_at,updated_at,deleted_at) VALUES
	 ('c2331ef3-d00d-496a-8d25-d4b46e3cece5','4751bd50-cc94-4182-b855-ea6895d547fb','PENDING','TRAVEL','3fa85f64-5717-4562-b3fc-2c963f66afa6','Renfe','',70,'FIXED','DIRECT_DEBIT',false,'e6a72a7e-8852-4238-a5f3-3ebb3a62547a','2023-09-09 02:15:13.482254','2023-09-09 02:15:13.482254',NULL);

INSERT INTO recurring_expense (id,user_id,status,category,recipient_id,concept,"comments",amount,amount_type,payment_method,frequency_type,frequency_parameter,first_payment_date,last_payment_date,hidden_in_plans,created_at,updated_at,deleted_at) VALUES
	 ('294ad750-8143-4631-89bc-767b2d4f42cb','4751bd50-cc94-4182-b855-ea6895d547fb','ACTIVE','RENT_AND_UTILITIES','3fa85f64-5717-4562-b3fc-2c963f66afa6','Alquiler Calle Marsha P. Johson, 9, 4º B','',700,'FIXED','DIRECT_DEBIT','MONTHLY_EXACT_DAY_OF_MONTH',1,'2022-08-01',NULL,false,'2023-09-09 02:10:20.976553','2023-09-09 02:10:20.976553',NULL),
	 ('10d74b40-d5f5-492d-bcf4-df579771dfad','4751bd50-cc94-4182-b855-ea6895d547fb','ACTIVE','RENT_AND_UTILITIES','103b184f-0da5-4f5e-94b7-c7970c8cd2e4','Paquete de telefonía e internet','',40,'FIXED','DIRECT_DEBIT','MONTHLY_UNKNOWN',NULL,'2022-08-01',NULL,false,'2023-09-09 02:10:20.976553','2023-09-09 02:10:20.976553',NULL),
	 ('b52b125d-d193-47ad-a596-acf4dc1139ac','4751bd50-cc94-4182-b855-ea6895d547fb','ACTIVE','ENTERTAINMENT','0752ca23-b729-471a-bab5-c7659cad12f1','Spotify Premium','',4.95,'FIXED','DIRECT_DEBIT','MONTHLY_UNKNOWN',NULL,'2022-08-01',NULL,false,'2023-09-09 02:10:20.976553','2023-09-09 02:10:20.976553',NULL);

INSERT INTO expense_payment (id,expense_id,status,amount,date,authorization_date) VALUES
	 ('e6a72a7e-8852-4238-a5f3-3ebb3a62547a','c2331ef3-d00d-496a-8d25-d4b46e3cece5','PENDING',70,'2023-09-09','2023-09-09'),
	 ('124c356b-06c3-49bb-ab93-1c33ae6ea15f','294ad750-8143-4631-89bc-767b2d4f42cb','POSTED',700,'2023-08-01','2023-08-01');
