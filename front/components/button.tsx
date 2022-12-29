import styles from "styles/button.module.scss";
import Link from "next/link";

type Props = {
  title: string;
  href?: string;
  color?: string;
};

export default function Button({ title, color, href }: Props) {
  return (
    <>
      <Link href={href || "#"}>
        <button
          style={{
            backgroundColor: color,
            borderColor: color,
          }}
          className={styles.container}
        >
          {title}
        </button>
      </Link>
    </>
  );
}
