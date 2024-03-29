# eAUrnik

REST API za urnike iz eAsistenta v formatu iCalendar. Vrne urnik za akutalni teden, od sobote naprej pa za naslednji.

## Namestitev

Potrebne knjižnjice se namesti z ukazom:

```
pip install flask_restful ics lxml requests
```

Za namen razvoja se strežnik lahko izvaja lokalno. Lokalni strežnik zaženemo z ukazom:

```
python API.py
```

Za dolgoročno uporabo se API naloži na strežnik (npr. strežniška storitev [Heroku](https://www.heroku.com)). [Več o tem](https://medium.com/@ashiqgiga07/deploying-rest-api-based-flask-app-on-heroku-part-1-cb43a14c50c).

## Uporaba

Povezava na urnik v eAsistentu je strukturirana sledeče:

```
https://www.easistent.com/urniki/SCHOOL/razredi/CLASS/dijak/STUDENT
```

Enako URL strukturo uporablja tudi eAUrnik. Primer uporabe lokalnega *development* strežnika:

```
http://127.0.0.1:5000/urniki/SCHOOL/razredi/CLASS/dijak/STUDENT
```

Povezava vodi do .ics datoteke z aktualnim tedenskim urnikom za podane parametre o šoli, razredu in dijaku.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

*"eAsistent" blagovna znamka podjetja eŠola d.o.o.*
