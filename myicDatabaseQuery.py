import sqlite3
from pathlib import Path

dbPath = Path(__file__).parent/"myic.db"

#connects to lifesuite.db
def getConnection():
    conn = sqlite3.connect(dbPath)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def createDatabase():
    conn = getConnection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS mood (
            moodID  INTEGER PRIMARY KEY AUTOINCREMENT,
            emotion TEXT,
            color   TEXT
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS entry (
            entryID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            date    TEXT,
            emotion TEXT    REFERENCES mood (emotion),
            notes   TEXT,
            time    TEXT
        );  
    """)

    conn.commit()
    conn.close()

#add new entry   
def myicAddDay(queryVariables):
    conn = getConnection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO entry (date, emotion, notes, time) VALUES (:date, :emotion, :notes, :time)", queryVariables)
        conn.commit()
    finally:
        conn.close()

#return all entries in entry table
def myicGetAllEntries():
    conn = getConnection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM entry")
        diary = cur.fetchall()
        for entry in diary:
            print(dict(entry))
    finally:
        conn.close

def myicGetSpecificEntry(viewID):
    conn = getConnection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM entry WHERE entryID = ?", viewID)
        diary = cur.fetchone()
        print(tuple(diary))
    finally:
        conn.close 

#delete specific entry
def myicDeleteEntry(deleteID):
    conn = getConnection()
    #check if deleteID is in the database
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM entry WHERE entryID = ?", deleteID)
    finally:
        conn.close

def myicEditEntry(editText,editID):
    editEntry = (editText,editID)
    conn = getConnection()
    #check if editID is in the database
    try:
        cur = conn.cursor()
        cur.execute("UPDATE entry SET notes = ? WHERE entryID = ?", editEntry)
        conn.commit()
    finally:
        conn.close

def myicGetMoods():
    conn = getConnection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM mood")
        mood = cur.fetchall()
        return mood
    finally:
        conn.close

def myicAddMood(mood):
    conn = getConnection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO emotions (color, emotion) VALUES (:color, :emotion)", mood)
        conn.commit()
    finally:
        conn.close
