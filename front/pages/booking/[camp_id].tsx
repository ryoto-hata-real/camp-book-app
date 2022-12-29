import Head from "next/head";
import React from "react";
import { GetStaticPaths, GetStaticProps } from "next";
import { NextPage } from "next";
import Link from "next/link";
import Image from "next/image";
import styles from "/styles/Book.module.scss";
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
  const camp_id = context.params!.camp_id as string;
  const res_camp_data = await axios.get(
    process.env.NEXT_PUBLIC_API_URL! + `users/${camp_id}`
  );
  const camp_data: CampResponse = res_camp_data.data;
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

const Book = ({ camp_id, camp_name, camp_email, camp_tel }: PageProps) => {
  type bookCampDataType = {
    client_id: number;
    booked_date: Date;
    customer_number: number;
    customer_name: string;
    customer_tel: string;
    customer_email: string;
    customer_remarks: string;
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    const { currentTarget } = event;
    event.preventDefault();
    const bookCampData = {
      client_id: Number(camp_id),
      booked_date: currentTarget.booked_date.value,
      customer_number: currentTarget.customer_number.value,
      customer_name: currentTarget.customer_name.value,
      customer_tel: currentTarget.customer_tel.value,
      customer_email: currentTarget.customer_email.value,
      customer_remarks: currentTarget.customer_remarks.value,
    };
    console.log(bookCampData);
    const bookCampResponse = bookCamp(bookCampData);
    console.log(bookCampResponse);
  };

  const bookCamp = async (bookCampData: bookCampDataType) => {
    await axios.post(
      process.env.NEXT_PUBLIC_API_URL! + `customer`,
      bookCampData
    );
  };
  return (
    <>
      <Header>
        <title>キャンプ場予約</title>
      </Header>
      <div className={styles.container}>
        <h1 className={styles.title}>キャンプ場名：{camp_name}</h1>
        <form onSubmit={handleSubmit} className={styles["book-form"]}>
          日付<input type="date" name="booked_date"></input>
          名前<input type="text" name="customer_name"></input>
          人数<input type="text" name="customer_number"></input>
          電話番号<input type="tel" name="customer_tel"></input>
          メールアドレス<input type="email" name="customer_email"></input>
          備考<input type="textarea" name="customer_remarks"></input>
          <button type="submit">予約する</button>
        </form>
      </div>
      <Footer />
    </>
  );
};

export default Book;
