from typing import Dict, List
import pymongo as pm


class MongoUtilities:

    def __init__(self, client, db):
        self.client = pm.MongoClient("mongodb://localhost:27017/")
        self.db = client.spy

    def get_all_hosts(self, db: pm.database) -> pm.cursor.Cursor:
        return db.hosts.find()

    def get_host_by_id(self, db: pm.database, host_id: str) -> Dict:
        return db.hosts.find_one({'id': str(host_id)})

    def get_all_guests(self, db: pm.database) -> pm.cursor.Cursor:
        return db.guests.find()

    def get_guest_by_id(self, db: pm.database, guest_id: str) -> Dict:
        return db.guests.find_one({'id': str(guest_id)})

    def remove_host_by_id(self, db: pm.database, host_id: str) -> Dict:
        return db.hosts.find_one_and_delete({'id': str(host_id)})

    def remove_guest_by_id(self, db: pm.database, guest_id: str) -> Dict:
        return db.guests.find_one_and_delete({'id': str(guest_id)})

    def add_host(self, db: pm.database, host: Dict) -> pm.results.InsertOneResult:
        return db.hosts.insert_one(host)

    def add_guest(self, db: pm.database, guest: Dict) -> pm.results.InsertOneResult:
        return db.guests.insert_one(guest)

    def update_host_by_id(self, db: pm.database,
                            host_id: str,
                            update: Dict) -> pm.results.UpdateResult:
        return db.hosts.update_one({'id': str(host_id)}, {"$set": update})

    def update_guest_by_id(self, db: pm.database,
                             guest_id: str,
                             update: Dict) -> pm.results.UpdateResult:
        return db.guests.update_one({'id': str(guest_id)}, {"$set": update})

    def get_matches_for_guest(self, db: pm.database, guest_id: str) -> pm.cursor.Cursor:
        return db.matchResults.find({'guestId': guest_id})

    def get_matches_for_host(self, db: pm.database, host_id: str) -> pm.cursor.Cursor:
        return db.matchResults.find({'hostId': host_id})

    def add_matches(self, db: pm.database, matches: List) -> pm.results.InsertOneResult:
        return db.matchResults.insert_many(match)

    def remove_match(self, db: pm.database, host_id: str, guest_id: str) -> Dict:
        return db.matchResults.find_one_and_delete({'guestId': guest_id},
                                                     {'hostId': host_id})
