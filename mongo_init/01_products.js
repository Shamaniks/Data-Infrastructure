db = db.getSiblingDB('shopdb');

db.products.insertOne({
  _id: 1,
  article_number: "SP/0000001",
  clothing_image: "/images/products/0000001.jpg",
  price: 299.99,
  clothing_type: "Футболка",
  season: "Летний",
  manufacturer: { name: "FugiStyle", country: "Таиланд" },
  composition: [
    { material: "хлопок", proportion: 60 },
    { material: "синтетика", proportion: 40 }
  ],
  available_sizes: ["M", "L", "XL"]
});

db.products.insertOne({
  _id: 2,
  article_number: "SP/0000002",
  clothing_image: "/images/products/0000002.jpg",
  price: 14000,
  clothing_type: "Пальто",
  season: "Осень-Зима",
  manufacturer: { name: "Пошивка", country: "Россия" },
  composition: [
    { material: "войлок", proportion: 70 },
    { material: "кашемир", proportion: 10 },
    { material: "подкладка", proportion: 20 }
  ],
  available_sizes: ["S", "M", "L", "XL"]
});

db.products.insertOne({
  _id: 3,
  article_number: "SP/0000003",
  clothing_image: "/images/products/0000003.jpg",
  price: 450,
  clothing_type: "Джемпер",
  season: "Осень",
  manufacturer: { name: "FugiStyle", country: "Таиланд" },
  composition: [
    { material: "шерсть", proportion: 90 },
    { material: "хлопок", proportion: 10 }
  ],
  available_sizes: ["XS", "S", "M", "L"]
});

db.products.insertOne({
  _id: 4,
  article_number: "SP/0000004",
  clothing_image: "/images/products/0000004.jpg",
  price: 1500,
  clothing_type: "Брюки",
  season: "Демисезонная",
  manufacturer: { name: "FugiStyle", country: "Таиланд" },
  composition: [
    { material: "лён", proportion: 100 }
  ],
  available_sizes: ["20", "22", "24", "26", "28"]
});

db.products.insertOne({
  _id: 5,
  article_number: "SP/0000005",
  clothing_image: "/images/products/0000005.jpg",
  price: 359.99,
  clothing_type: "Поясной ремень",
  season: "Демисезонная",
  manufacturer: { name: "GRT", country: "Китай" },
  composition: [
    { material: "кожа", proportion: 65 },
    { material: "кожзаменитель", proportion: 35 }
  ],
  available_sizes: ["100 см", "120 см"]
});
