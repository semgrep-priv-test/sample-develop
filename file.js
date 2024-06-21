let tryAgainButtonEl: HTMLElement;

window.onload = () => {
  getElements();
  listenForTryAgainClick();
};

export function listenForTryAgainClick(): void {
  if (tryAgainButtonEl) {
    tryAgainButtonEl.addEventListener('click', tryAgain);
  }
}

function tryAgain(): void {
  const postLogoutUrl = getQueryParamValue('post_logout_url');
  const queryParams = { invalidate_tokens: 'true', target_url: postLogoutUrl || '' };
  const searchParams = new URLSearchParams(queryParams);
  window.location.href = `${window.location.origin}/am/tide/logout?${searchParams}`;
}

function getQueryParamValue(name: string): string | null {
  return new URLSearchParams(window.location.search).get(name);
}

export function getElements(): void {
  tryAgainButtonEl = document.getElementById('try-again')!;
}
