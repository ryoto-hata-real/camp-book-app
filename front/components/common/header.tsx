import styles from "../../styles/header.module.scss";
import Link from "next/link";
import Head from "next/head";
import { ReactNode } from "react";

type Props = {
  children: ReactNode;
};
export default function Header({ children }: Props) {
  return (
    <>
      <Head>
        {children}
        <link rel="icon" href="/favicon.ico" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1.0"
        ></meta>
      </Head>
      <header>
        <div className={styles["header-nav"]}></div>
      </header>
    </>
  );
}
