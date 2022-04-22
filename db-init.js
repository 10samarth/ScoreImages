db = db.getSiblingDB("cards");
db.cards.drop();

db.cards.insertMany([
    {
        'card_id':'1',
        'image_name':'angular.png',
        'score':0
    },
    {
        'card_id':'2',
        'image_name':'react.png',
        'score':0
    },
    {
        'card_id':'3',
        'image_name':'logo.png',
        'score':0
    },
    {
        'card_id':'4',
        'image_name':'svelte.png',
        'score':0
    }
    ]);