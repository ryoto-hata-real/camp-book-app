import Head from "next/head";
import React from "react";
import { GetServerSideProps } from "next";

//　TODO: 関数に渡すパラメとしてID、人数、電話番号などを追加する
type PathParams = {
  camp_id: string;
};
type PageProps = {
  camp_name: string;
};

export const getServerSideProps: GetServerSideProps<PageProps> = async (
  context
) => {
  const { camp_id } = context.params as PathParams;

  const props: PageProps = {
    camp_name: "キャンプ場名",
  };
  // 引数からキャンプ場の予約関数を実行
  return { props };
};
export const BookComplete = ({ camp_name }: PageProps) => {};
