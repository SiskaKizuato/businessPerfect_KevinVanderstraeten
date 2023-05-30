from django_seed import Seed    
from app.models import BlogPost, PortfolioPost
import random
import faker

def run():
    seeder = Seed.seeder()
    fake = faker.Faker()
    
    seeder.add_entity(BlogPost, 4, {
        'title' : lambda x: seeder.faker.sentence(nb_words=3),
        'img' : lambda x : seeder.faker.image_url(),
        'description' : lambda x : seeder.faker.text()
    })
    
    seeder.add_entity(PortfolioPost, 15, {
        'title' : lambda x: seeder.faker.sentence(nb_words=3),
        'description' : lambda x: seeder.faker.text()
    })
    
    inserted_pks = seeder.execute()
    print(inserted_pks)
