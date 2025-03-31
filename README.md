# Kwadrat-Logiczny
***Projekt IO***

Użytkownik podaje zdanie dotyczące stanu np. 'Każdy samolot stoi na płycie lotniska'. Program wysyła prompt i podaje przykładowe wierzchołki kwadratu logicznego (KL) zgodnie z zasadami zdań kategorycznych i KL. Użytkownik może akceptować propozycje lub odeprzeć.


**Uwaga**

Do preojketu został stworzony nowy model LLM: *KL_LLM* który znajduje się w pliku ./modifle. Został stworzony, aby skupić LLM na temat kwdartu logicnzego i gramatyki. Do projektu trzeba pobrać Olama, następnie llama3:1b, albo llama3:3b. Następnie w CMD w folderze programu wpisać **ollama create KL_LLM -f ./modefile**.


**Język**: Python

***LLM***: Ollama, llama3:1b, llama3:3b