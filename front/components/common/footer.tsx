import styles from "../../styles/footer.module.scss";
import Link from "next/link";
import Head from "next/head";
import { ReactNode } from "react";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles["header-nav"]}></div>
    </footer>
  );
}
