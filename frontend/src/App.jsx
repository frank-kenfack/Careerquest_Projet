import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [missions, setMissions] = useState([]);
  const [avatar, setAvatar] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // On lance les deux requêtes en même temps pour aller plus vite !
    Promise.all([
      axios.get('http://localhost:8000/api/missions/'),
      axios.get('http://localhost:8000/api/avatars/')
    ])
    .then(([missionsResponse, avatarsResponse]) => {
      setMissions(missionsResponse.data);
      // On prend le premier avatar de la liste pour simuler l'utilisateur connecté
      if (avatarsResponse.data.length > 0) {
        setAvatar(avatarsResponse.data[0]);
      }
      setLoading(false);
    })
    .catch((error) => {
      console.error("Erreur de communication avec l'API:", error);
      setLoading(false);
    });
  }, []);

  if (loading) return <div style={{ padding: '20px' }}>Chargement du jeu...</div>;

  return (
    <div style={{ maxWidth: '1000px', margin: '0 auto', padding: '20px', fontFamily: 'system-ui, sans-serif' }}>
      <h1 style={{ textAlign: 'center', color: '#2c3e50' }}>🚀 CareerQuest</h1>
      
      {/* --- SECTION AVATAR --- */}
      {avatar && (
        <div style={{ 
          backgroundColor: '#2c3e50', 
          color: 'white', 
          padding: '20px', 
          borderRadius: '10px',
          marginBottom: '30px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <div>
            <h2 style={{ margin: '0 0 10px 0' }}>👤 {avatar.user.username}</h2>
            <p style={{ margin: 0, color: '#bdc3c7' }}>Apparence : {avatar.appearance_display}</p>
          </div>
          <div style={{ textAlign: 'right' }}>
            <h2 style={{ margin: '0 0 5px 0', color: '#f1c40f' }}>Niveau {avatar.level}</h2>
            <p style={{ margin: 0, fontWeight: 'bold' }}>✨ {avatar.current_xp} XP</p>
          </div>
        </div>
      )}

      {/* --- SECTION MISSIONS --- */}
      <h2 style={{ color: '#34495e' }}>📜 Quêtes Disponibles</h2>
      <div style={{ display: 'grid', gap: '15px', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))' }}>
        {missions.map((mission) => (
          <div key={mission.id} style={{ 
            border: '1px solid #e0e0e0', 
            padding: '20px', 
            borderRadius: '8px',
            backgroundColor: 'white',
            boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
          }}>
            <h3 style={{ marginTop: 0, color: '#2980b9' }}>{mission.title}</h3>
            <div style={{ marginBottom: '15px' }}>
              <span style={{ backgroundColor: '#ecf0f1', color: '#7f8c8d', padding: '4px 8px', borderRadius: '4px', fontSize: '0.85em', marginRight: '10px' }}>
                {mission.quest_type_display}
              </span>
              <span style={{ color: '#27ae60', fontWeight: 'bold', fontSize: '0.9em' }}>
                + {mission.xp_reward} XP
              </span>
            </div>
            <p style={{ color: '#555', fontSize: '0.95em', lineHeight: '1.5' }}>{mission.description}</p>
            
            <button style={{
              width: '100%',
              padding: '10px',
              backgroundColor: '#3498db',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
              fontWeight: 'bold',
              marginTop: '10px'
            }}>
              Accomplir la mission
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;