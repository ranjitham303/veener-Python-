class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
      return '{artist}. "{title}". {medium}, {year}. {name}, {location}'.format(artist=self.artist, title=self.title, medium=self.medium, year=self.year, name=self.owner.name, location=self.owner.location)

class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self,remove_listing):
    self.listings.remove(remove_listing)
    
  def show_listing(self):
    for lists in self.listings:
      print(lists)
   
  
class Client:
  def __init__(self, name, location, is_museum, wallet):
    self.name = name
    self.wallet = wallet
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = 'Private Collection'
   
  def sell_artwork(self, artwork, price, wallet):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
      
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
    if art_listing != None:
      art_listing.art.owner = self
      veneer.remove_listing(art_listing)
      
      
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '{n}, {p}'.format(n=self.art.title, p=self.price)

veneer = Marketplace()


edytta = Client('Edytta Halpirt', None, False, 0)
moma = Client('The MOMA', 'New york', True, 0)

girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 1910, 'oil in canvas', edytta)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, '6M (USD)', 100)
veneer.show_listing()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)