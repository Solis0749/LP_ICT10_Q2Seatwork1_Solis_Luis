from pyscript import document

def candidate_checker(e):
    club_members = ['luis solis', 'becca vinco', 'athena silva', 'mikey robles', 'rj magno', 'jacob opilla', 'pio serdeña', 'max calata', 'simone tinio', 'ila martinez']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list', 
                f'Congratulations!, {candidate} You are now part of the Glee Club')

    document.getElementById('result').innerHTML = messages[member_checker] 