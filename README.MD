PGBACKUP command line utility
=

CLI fro backing up PostgreSQL DB to S3 or locally

Preparing for development
-

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repo ``git clone https://github.com/drewripa/pgbackup.git``
3. ``cd`` into repo folder
4. Fetch development dependencies ``make install``
5. Activate vitrualenv: ``pipenv shell``

Usage
-

Pass in a full database URL, the storage driver, and the destination

S3 Example w/ bucket name:


    $ pgbackup postgres://user@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:


    $ pgbackup postgres://user@example.com:5432/db_one --driver local /var/local/db_one/bkp/dump.sql

Running tests 
-

Run test locally using ``make`` if vitrualenv is active:

    $ make
    
In virtualenv isn't active then use:

    $ pipenv run make