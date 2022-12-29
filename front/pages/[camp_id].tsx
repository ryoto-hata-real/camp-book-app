import Head from "next/head";
import React from "react";
import { GetStaticPaths, GetStaticProps } from "next";
import { NextPage } from "next";
import Link from "next/link";
import Image from "next/image";
import styles from "styles/Home.module.scss";
import Button from "@/components/button";
import Header from "@/components/common/header";
import Footer from "@/components/common/footer";

import axios from "axios";

type PathParams = {
  camp_id: string;
};

type PageProps = {
  camp_id: string;
  camp_name: string;
  camp_email: string;
  camp_tel: string;
};

type CampResponse = {
  client_name: string;
  client_id: number;
  default_amount: number;
  client_tel: string;
  price: number;
  client_email: string;
};

export const getStaticPaths: GetStaticPaths<PathParams> = async () => {
  const res = await axios.get(process.env.NEXT_PUBLIC_API_URL! + "users/");
  const camps: Array<CampResponse> = res.data;
  const paths = [];

  for (let camp of camps) {
    paths.push({ params: { camp_id: String(camp.client_id) } });
  }

  return {
    paths,
    fallback: false,
  };
};

export const getStaticProps: GetStaticProps<PageProps> = async (context) => {
  const camp_id = context.params?.camp_id as string;

  const res = await axios.get(
    process.env.NEXT_PUBLIC_API_URL! + `users/${camp_id}`
  );
  const camp_data: CampResponse = res.data;
  const props: PageProps = {
    camp_id: camp_id,
    camp_name: camp_data.client_name,
    camp_email: `Email-${camp_data.client_email}`,
    camp_tel: `Tel-${camp_data.client_tel}`,
  };

  // ページコンポーネントに渡す PageProps オブジェクトを
  // props プロパティに設定したオブジェクトを返す
  return { props };
};

const Home = ({ camp_id, camp_name, camp_email, camp_tel }: PageProps) => {
  return (
    <>
      <Header>
        <title>キャンプ場詳細</title>
      </Header>
      <div className={styles.container}>
        <h1 className={styles.title}>キャンプ場名：{camp_name}</h1>
        <Image src={""} alt={""} />

        <div>電話番号: {camp_tel}</div>
        <div>住所</div>
        <Button
          title="予約する"
          color="#f05753"
          href={`/booking/${camp_id}`}
        ></Button>
      </div>
      <Footer />
    </>
  );
};

export default Home;
