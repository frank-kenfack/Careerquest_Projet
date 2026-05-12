import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  // 1. On prepare une "boite" (state) pour ranger nos missions
  const [missions, setMissions] = useState([]);
  const [loading, setLoading] = useState(true);

  // 2. On utilise useEffect pour aller chercher les donnees au chargement de la page
  useEffect(() => {
    // On appelle notre API Django
    axios.get('http://localhost:8000/api/missions/')
      .then((response) => {
        // On range les donnees recues dans notre boite
        setMissions(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des missions:", error);
        setLoading(false);
      });
  }, []); // Le tableau vide [] signifie "Fais-le une seule fois au demarrage"

  // 3. Ce qu'on affiche e l'ecran
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1> Tableau des Missions - CareerQuest</h1>
      
      {loading ? (
        <p>Chargement des quêtes depuis le serveur...</p>
      ) : (
        <div style={{ display: 'grid', gap: '15px', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))' }}>
          {/* On boucle sur chaque mission pour l'afficher */}
          {missions.map((mission) => (
            <div key={mission.id} style={{ 
              border: '1px solid #ccc', 
              padding: '15px', 
              borderRadius: '8px',
              backgroundColor: '#f9f9f9'
            }}>
              <h2 style={{ marginTop: 0, color: '#2c3e50' }}>{mission.title}</h2>
              <span style={{ 
                backgroundColor: '#3498db', 
                color: 'white', 
                padding: '4px 8px', 
                borderRadius: '4px',
                fontSize: '0.8em'
              }}>
                {mission.quest_type_display}
              </span>
              <span style={{ 
                marginLeft: '10px',
                color: '#27ae60',
                fontWeight: 'bold'
              }}>
                 {mission.xp_reward} XP
              </span>
              <p>{mission.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;