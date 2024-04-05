get ebird bird name and bird ID
- go to https://ebird.org/barchart?byr=1900&eyr=2024&bmo=1&emo=12&r=AU-NSW
- run javascript
```javascript
$('.SpeciesName a').each(function(){console.log($(this).text().trim() + "," + $(this).attr('href').substr(9))})
```