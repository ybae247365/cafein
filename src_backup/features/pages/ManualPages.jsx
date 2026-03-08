import React, { useEffect, useState } from "react";
import api from "../../../lib/api"; // 팀 공용 axios 인스턴스 사용

const ManualPage = () => {
  const [manuals, setManuals] = useState([]); // 데이터를 담을 바구니
  const [loading, setLoading] = useState(true); // 로딩 중인지 확인

  // 페이지가 처음 열릴 때 데이터를 가져오는 함수 실행
  useEffect(() => {
    fetchManuals();
  }, []);

  const fetchManuals = async () => {
    try {
      const response = await api.get("/api/manual/list");
      setManuals(response.data); // 성공하면 바구니에 담기
    } catch (error) {
      console.error("데이터를 못 가져왔어요:", error);
    } finally {
      setLoading(false); // 로딩 끝
    }
  };

  if (loading) return <div className="p-10">로딩 중입니다...</div>;

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">☕ 업무 매뉴얼</h1>

      {/* 카테고리별로 카드를 예쁘게 나열합니다 */}
      <div className="grid gap-4">
        {manuals.map((item) => (
          <div
            key={item.id}
            className="border p-4 rounded-lg shadow-sm hover:bg-gray-50 transition"
          >
            <span className="text-xs font-semibold px-2 py-1 bg-espresso text-white rounded uppercase">
              {item.category}
            </span>
            <h2 className="text-lg font-bold mt-2">{item.title}</h2>
            <p className="text-gray-600 line-clamp-2 mt-1">{item.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ManualPage;
