# RandGen - Website Design

## Process

### Public Service

Every visitor is allowed to generate random numbers in a special range.
All the generations will be stored in a database and visible to all visitors.
Users can choose the nickname they want to be recorded.

Every **Entry** will be stored with these info:

- User's nickname
- Timestamp
- Range
- Result
- Special HASH code
- Unauthorized mark

### Verified Users Service

Verified users will get 10 UUID at a time. 
They can use these UUIDs to generate verified random number.
It means that they cannot generate multiple times to get a special number.
Every use of UUID-Generation will be supervised because these record will be cited as **Verified**.

- Verified username
- Timestamp
- Range
- Result
- Special HASH code
- Unauthorized mark

## Structure

The website front-end is made using templates with Flask.
Entries are stored using SQLite.

## Pages

### Index

Top Half: Users can give their nickname and range, and push the GENERATE button to create a random number.
Users can also give their UUID if they have one. If the UUID is valid, their customized nickname won't be shown.

Bottom Half: Displaying latest 5 generation records, and a link to "Record" pages.

### Record

Showing all the records.

### Record/Public

Showing public records only.

### Record/Verified

Showing verified records only.

