# [🧾Expenses Tracker Streamlit App💶](https://expensestrackerr.streamlit.app/)
<p align="left"> 
    <a href="https://share.streamlit.io/">
        <img width="140" src="assets/img/streamlit_icon.png" align="left"></img>
    </a>
    <a href="https://app.netlify.com/teams/smdlabtech">
        <img width="90"src="assets/img/senlab_ia_gen.ico" align="left"></img>
    </a>
</p><br><br><br><br><br>

Pour lancer lancer l'application veuillez cliquez sur ce lien : [➡️ Expenses Tracker Streamlit App](https://expensestrackerr.streamlit.app/)  
🚀 Deployer une application sur Streamlit : [➡️ docs.com](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)  
Pour suivre toutes les étapes appliquées pour réaliser cette application, veuillez [➡️ cliquez-ici📌](demarches.md).
<p align="left"> 
Retrouver toutes les applications listées dans le <strong>Gestionnaire de Tâches.</strong>
    <a href="https://www.notion.so/1537fdac3335403d81dabe8198c02f72">
        <img width = "20" src="assets/img/Notion-logo.png" align="left"></img>
    </a>
</p><br>


<!--------------------->
### 💡 Conseils : 
Avant de faire chaque ***commit***, pensez à éxécuter la commande suivante pour mettre à jour la documentation des fonctions, [⚙️```dev_documentations.md```](/dev_documentations.md) : 
```javascript copy
python dev_generate_docs.py
```

Architechture de l'application :   

```css copy
expenses_tracker_streamlit/
│
├── _pages/
│   ├── details.py
│   ├── overview.py
│   ├── homepage.py
│   ├── raw_data.py
├── __data/
│   ├── data_brsma/
│   ├── data_lcl/
├── __docs/
│   ├── expenses_tracker_app_pbi_desktop.pdf
├── assets/
│   ├── css/
│   ├── html/
│   ├── img/
│   ├── js/
├── app_styles.py
├── app_data_loader.py
├── app.py
├── README.md
├── dev_documentations.md
├── dev_generate_docs.py
├── requirements.txt
```

