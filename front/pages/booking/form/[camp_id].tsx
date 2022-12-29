import Head from "next/head";
import React from "react";
import { GetStaticPaths, GetStaticProps } from "next";
import { NextPage } from "next";
import Link from "next/link";
import Image from "next/image";
import styles from "../styles/Home.module.scss";
import Button from "../../../components/button";
import Header from "../../../components/common/header";
import Footer from "../../../components/common/footer";

type PathParams = {
  camp_id: string;
};

type PageProps = {
  camp_name: string;
  camp_email: string;
  camp_tel: string;
};

export const getStaticPaths: GetStaticPaths<PathParams> = async () => {
  return {
    paths: [
      { params: { camp_id: "001" } },
      { params: { camp_id: "002" } },
      { params: { camp_id: "003" } },
    ],
    fallback: false,
  };
};

export const getStaticProps: GetStaticProps<PageProps> = async (context) => {
  // ファイル名が [id].tsx なので id パラメーターを取り出すことができる
  const { camp_id } = context.params as PathParams;

  // 本来はここで getBook(id) のように API を呼び出してデータを取得する
  const props: PageProps = {
    camp_name: `Title-${camp_id}`,
    camp_email: `Email-${camp_id}`,
    camp_tel: `Tel-${camp_id}`,
  };

  // ページコンポーネントに渡す PageProps オブジェクトを
  // props プロパティに設定したオブジェクトを返す
  return { props };
};

const Home = ({ camp_name, camp_email, camp_tel }: PageProps) => {
  return (
    <>
      <Header>
        <title>キャンプ場予約</title>
      </Header>
      <div className={styles.container}>
        <h1 className={styles.title}>キャンプ場名：{camp_name}</h1>
        <Image src={""} alt={""} />

        <div>電話番号: {camp_tel}</div>
        <div>住所</div>
        <Button
          title="予約する"
          color="#f05753"
          href="/posts/first_post"
        ></Button>
      </div>
      <Footer />
    </>
  );
};

export default Home;
