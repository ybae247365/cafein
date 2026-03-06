import React, { useEffect, useState } from "react";
import "./ManualList.css"; // 아래에서 만들 스타일 파일

const ManualList = () => {
  const [manuals, setManuals] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // 백엔드 서버 주소로 데이터 요청
    fetch("http://localhost:8001/api/manual/list")
      .then((response) => response.json())
      .then((data) => {
        setManuals(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("데이터를 못 가져왔어요:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="loading">카페 메뉴 불러오는 중...</div>;

  return (
    <div className="manual-list-container">
      <h2>☕ 카페인 메뉴판</h2>
      <div className="manual-grid">
        {manuals.map((item) => (
          <div key={item.id} className="manual-card">
            <h3>{item.item_name}</h3>
            <p className="price">{item.price.toLocaleString()}원</p>
            <button className="detail-btn">상세보기</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ManualList;
