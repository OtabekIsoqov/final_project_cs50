#RUN PYTEST: python -m pytest test_file_name.py
from project import n_customers, now, get_user_info

def test_n_customers(monkeypatch):
    #case 1: 
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert n_customers() == 1 

    #case 1: 
    inputs = iter(['3', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert n_customers() == 2 
    
    #case 2: 
    inputs = iter(['cat', 'dog', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert n_customers() == 2

def test_now(capsys):
    now()
    captured_output = capsys.readouterr()
    assert "Date/time as of now in Rome/Italy" in captured_output.out
    assert "You can see available date/times starting from next week," in captured_output.out

def test_get_user_info(monkeypatch): 
    #case 1:
    inputs = iter(["otabek", "isoqov", "9876543210"]) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 
    some_list = [] 
    result = get_user_info(some_list, 1) 
    assert result == [["Otabek", "Isoqov", "+399876543210"]] 

    #case 2:
    inputs = iter([
            "aMiRhOSEIN", "SABeri", "1234567890",
            "RUZIvoy", "qosimov", "1231567890"
    ])    
    
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 
    some_list = [] 
    result = get_user_info(some_list, 2) 
    assert result == [
        ["Amirhosein", "Saberi", "+391234567890"],
        ["Ruzivoy", "Qosimov", "+391231567890"]
    ]

    #case 3: 
    inputs = iter(["91dasd///", "bek", "isoqov", "9876", "9876543210"]) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 
    some_list = [] 
    result = get_user_info(some_list, 1) 
    assert result == [["Bek", "Isoqov", "+399876543210"]]