AGUSTINO LARA'S XML EXAMPLE
===========================

What is XML example code about?:
--------------------------------

The XML example code provides structured data representation of **League of Legends champions**. It simulates how champion information might be stored or shared in a machine-readable format using XML. Each `<champion>` element contains detailed metadata such as:

- **Name** and **Title** (what the champion is known as)
- **Role** (their typical in-game function, e.g., Mage, Tank)
- **Region** (the faction or area they originate from in the game's lore)
- **Difficulty level** (how hard they are to play)
- **Release date** and **Price** (representing availability and cost)
- **Voice line** (signature quote that reflects their personality)
- **Lore** (backstory that explains their motivation and history)

This XML structure is ideal for developers, data parsers, or game databases who want to organize character information in a way that can be easily processed or displayed on websites, mobile apps, or game companion tools.


Viktor
------

.. image:: https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Viktor_0.jpg
   :alt: Viktor Splash Art
   :width: 720px
   :align: center

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <league>
     <champion id="Viktor">
       <name>Viktor Magtanggol</name>
       <title>the Herald of the Arcane</title>
       <role>Mage</role>
       <region>Zaun</region>
       <difficulty>Hard</difficulty>
       <release_date>December 11, 2024</release_date>
       <price currency="BE">4800</price>
       <voice_line>"Humanity can be so much more."</voice_line>
       <lore>
         <b> Viktor is a visionary who dedicated his life to the advancement of humankind. Through technology, he aims to elevate society beyond its frail limitations.</b>
         </lore>
      </champion>
   </league>

**REFERENCE**: https://www.leagueoflegends.com/en-ph/champions/viktor/


------


Dr. Mundo
---------

.. image:: https://ddragon.leagueoflegends.com/cdn/img/champion/splash/DrMundo_0.jpg
   :alt: Corporate Mundo
   :width: 720px
   :align: center

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <league>
     <champion id="Dr.Mundo">
       <name>Doctor "Mundo" Edmundo</name>
       <title>The Madman of Zaun</title>
       <role>Tank/Fighter</role>
       <region>Zaun</region>
       <difficulty>Medium</difficulty>
       <release_date>September 2, 2009</release_date>
       <price currency="BE">3150</price>
       <voice_line>"No worry. Me doctor!"</voice_line>
       <lore>
         <b>Driven by his own twisted version of medicine, Dr. Mundo passively regenerates health and charges into enemies with reckless abandon.</b>
       </lore>
     </champion>
   </league>

**REFERENCE**: https://www.leagueoflegends.com/en-ph/champions/drmundo/
