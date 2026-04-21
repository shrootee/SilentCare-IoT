import React, { useState } from 'react';

// Reflecting the "Silent Vibration" and "RGB LED" indicators [cite: 6, 20]
const SilentCareDashboard = () => {
  const [beds, setBeds] = useState([
    { id: 101, status: 'Normal', hr: 72, color: 'green' },
    { id: 102, status: 'Critical', hr: 125, color: 'red' }
  ]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>SilentCare: Central Monitoring Dashboard</h1>
      <div style={{ display: 'flex', gap: '20px' }}>
        {beds.map(bed => (
          <div key={bed.id} style={{ border: `2px solid ${bed.color}`, padding: '15px', borderRadius: '10px' }}>
            <h2>Bed {bed.id}</h2>
            <p>Heart Rate: {bed.hr} BPM</p>
            <p>Status: {bed.status}</p>
            {bed.status === 'Critical' && <button>Mute Vibration Alert</button>}
          </div>
        ))}
      </div>
    </div>
  );
};

export default SilentCareDashboard;