
mkdir templates 
python3 scaffold.py language name short_name
python3 scaffold.py musicalinstrument name
python3 scaffold.py musicalinstrumentpart musicalinstrument_id:references name language_id:references
python3 scaffold.py scoreparts name language_id:references musical_part:radio
python3 scaffold.py translation_score_parts scoreparts_id:references language_id:references content
python3 scaffold.py translation_musicalinstrumentpart musicalinstrumentpart_id:references language_id:references content
