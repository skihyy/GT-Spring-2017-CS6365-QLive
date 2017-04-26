# GT-Spring-2017-CS6365-QLive

## Installation
1. Create python virtual environment for Flask and other run time environment by `virtualenv environment --no-site-packages`. If flask has already been installed, or you are okay with flask being installed in the system, please ignore this step.
2. Activate the environment by `source environment/bin/activate`; deactivate by `deactivate`.
3. Install Flask by `pip install flask`.
4. Install the database by either running the function in `dao.py` (line #`16`), or build the table by yourself (the table structure has been in `schema.sql`).
4. Start server by `python flaskr_view_controller.py`.
5. To delete the temporary run time environment, simply delete `/environment` folder.

## Preinstalled Test Data
1. There are already 6 users, from `test1@test.com` to `test6@test.com` with all same password `123456`.
2. There are already 2 live sessions in the database, belongs to `test1` user and `test4` user.
