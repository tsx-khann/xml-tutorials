AGUSTINO LARA'S XML EXAMPLE
===========================

What is XML example code about?
-------------------------------

The XML example code provides structured data representation of **League of Legends champions**. It simulates how champion information might be stored or shared in a machine-readable format using XML. Each `<champion>` element contains detailed metadata such as:

- **Name:** and **Title:** .what the champion is known as.
- **Role:** their typical in-game function, e.g., Mage, Tank.
- **Region:** the faction or area they originate from in the game's lore.
- **Difficulty level:** how hard they are to play.
- **Release date:** date release ingame.
- **Price:** The cost of unlocking the champion in the game, both in terms of in-game currency (BE) and real money (RP).
- **Voice line:** signature quote that reflects their personality.
- **Lore:** backstory that explains their motivation and history.
- **Abilities:** The unique skills or powers each champion can use in-game, such as passive abilities and active skills.

This XML structure is ideal for developers, data parsers, or game databases who want to organize character information in a way that can be easily processed or displayed on websites, mobile apps, or game companion tools.

------

Viktor
------

.. image:: https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Viktor_0.jpg
   :alt: Viktor Splash Art
   :width: 720px
   :align: center

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <league>
     <champion id="viktor">
       <name>Viktor Magtanggol</name>
       <title>the Herald of the Arcane</title>
       <role>Mage</role>
       <region>Zaun</region>
       <difficulty>Hard</difficulty>
       <release_date>December 11, 2024</release_date>
       <price>
         <ingame currency="BE">4800</ingame>
         <real_money currency="RP">880</real_money>
       </price>
       <real_money currency="RP"> 880</real_money>
       <voice_line>"Humanity can be so much more."</voice_line>
       <lore>
         <b>Viktor is a visionary who dedicated his life to the advancement of humankind. Through technology, he aims to elevate society beyond its frail limitations.</b>
       </lore>

       <abilities>
         <PASSIVE>Glorious Evolution</PASSIVE>
         <Ability_1>Siphon Power</Q>
         <ability_2>Gravity Field</W>
         <ability_3>Death Ray</E>
         <Ultimate>Chaos Storm</R>
       </abilities>
     </champion>
   </league>

**REFERENCE**: https://www.leagueoflegends.com/en-ph/champions/viktor/

------

Volibear
---------

.. image:: https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Volibear_0.jpg
   :width: 720px
   :align: center

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <league>
     <champion id="volibear">
       <name>Volibear, the Relentless Storm</name>
       <title>The Relentless Storm</title>
       <role>Tank/Fighter</role>
       <region>Freljord</region>
       <difficulty>Medium</difficulty>
       <release_date>May 12, 2010</release_date>
       <price>
         <ingame currency="BE">1350</ingame>
         <real_money currency="RP">585</real_money>
       </price>
       <voice_line>"I will not be stopped!"</voice_line>
       <lore>
         <b>Once a proud spirit of the Freljord, Volibear was betrayed by his own tribe, forcing him to become a force of nature that tramples his enemies beneath his storm-ravaged feet.</b>
       </lore>
       <abilities>
         <PASSIVE>The Relentless Storm</PASSIVE>
         <ability_1>Thundering Smash</Q>
         <ability_2>Frenzied Maul</W>
         <ability_3>Sky Splitter</E>
         <Ultimate>Stormbringer</R>
       </abilities>
     </champion>
   </league>

**REFERENCE**: https://www.leagueoflegends.com/en-ph/champions/volibear/

