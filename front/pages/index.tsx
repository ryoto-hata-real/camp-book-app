import { NextPage } from "next";
import Head from "next/head";
import Link from "next/link";
import Image from "next/image";
import styles from "../styles/Home.module.scss";
import Button from "../components/button";
import Header from "../components/common/header";
import Footer from "../components/common/footer";

const Home: NextPage = () => {
  return (
    <>
      <Header>
        <title>キャンプ場詳細</title>
      </Header>
      <div className={styles.container}>
        <h1 className={styles.title}>キャンプ場名：あああああ</h1>
        <Image src={""} alt={""} />

        <div>電話番号</div>
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
